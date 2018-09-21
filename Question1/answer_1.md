To audit a model in django

Add a modified_at, modified_by, created_at and created_by to the model being audited and the audit log model.
Using a pre_save signal, re-retrieve the object that is about to be saved. Compare all fields of the two objects,
utilising the dict attribute of the model object ignoring any internal django data and create a diff, store the
changes possibly in a json field in an audit log table.


- For saving the time of the change

```
created_at = models.DateTimeField(auto_now_add=True)
modified_at = models.DateTimeField(auto_now=True)
```

- For retrieving the user is more tricky but using a package such as django-cuser makes it alot simpler
```
created_by = CurrentUserField(add_only=True)
modified_by = CurrentUserField()
```

- For the pre save signal I'd follow 
https://docs.djangoproject.com/en/2.1/topics/signals/#connecting-to-signals-sent-by-specific-senders