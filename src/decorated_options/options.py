from functools import wraps
import inspect


# TODO: Make pickeable; will involve adding '__getstate__'
class Options(object):
    """An immutable place to save options for a simulation run."""
    def __init__(self, **kwargs):
        """Pass the options to save using the """
        super(Options, self).__setattr__('_internal_options_data', kwargs)

    def __setattr__(self, attr, v):
        raise NotImplementedError('Cannot set values. Use "update" instead.')

    def __getattr__(self, attr):
        return self._internal_options_data[attr]

    def __contains__(self, k):
        return k in self._internal_options_data

    def keys(self):
        return self._internal_options_data.keys()

    def get(self, key):
        return self._internal_options_data[key]

    def set(self, *args, **kwargs):
        """Change values on the option."""
        if len(args) == 2:
            return self._update(**{args[0]: args[1]})
        else:
            return self._update(**kwargs)

    def set_new(self, *args, **kwargs):
        """Set a new value on the option."""
        if len(args) == 2:
            return self._update_with_new_keys(**{args[0]: args[1]})
        else:
            return self._update_with_new_keys(**kwargs)

    def _get_dict(self):
        return self._internal_options_data.copy()

    def _update_with_new_keys(self, **kwargs):
        d = self._get_dict()
        d.update(kwargs)
        return Options(**d)

    def _update(self, **kwargs):
        for k in kwargs:
            if k not in self._internal_options_data:
                raise ValueError("Key {} not present in original options.".format(k))

        return self._update_with_new_keys(**kwargs)


def optioned(option_arg='_opts'):
    """Returns a decorator which can 'fill-in' the arguments to function 'f' using the
    option passed in with the name given by `option_arg` parameter.

    :param: option_arg: The name of the argument which will contain the Options object.
    """
    def _decorator(f):
        sig = inspect.signature(f)
        params = sig.parameters
        f_args = params.keys()

        @wraps(f)
        def wrapped_f(*args, **kwargs):
            if option_arg not in kwargs:
                return f(*args, **kwargs)
            else:
                opts = kwargs[option_arg]
                all_args_dict = opts._get_dict()
                all_args_dict.update(kwargs)

                new_arg_dict = {}
                for idx, arg in enumerate(f_args):
                    if idx < len(args):
                        # This argument was passed positionally, ignore
                        pass
                    else:
                        if arg in all_args_dict:
                            new_arg_dict[arg] = all_args_dict[arg]
                        elif params[arg].default is not inspect._empty:
                            new_arg_dict[arg] = params[arg].default

                return f(*args, **new_arg_dict)

        return wrapped_f

    return _decorator
