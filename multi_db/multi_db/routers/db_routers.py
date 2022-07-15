class AuthRouter:
    """
    A router to control all database operations on models in the user application.
    """
    route_app_labels={'auth','contenttypes','session','admin'}

    def db_for_read(self,model,**hints):
        """
        Attempts to read user models go to users_db
        """
        if model._meta.app_label in self.route_app_labels:
            return 'my_db'
        return None

    def db_for_write(self,model,**hints):
        if model._meta.app_label in self.route_app_labels:
            return 'my_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if(obj1._meta.app_label in self.route_app_labels or obj2._meta.app_label in self.route_app_labels):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db=='my_db'
        return None

class MultipleDatabaseApp:
    route_app_labels ={'user_data'}

    def db_for_read(self,model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'users_data'

        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'users_data'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'users_data'
        return None

class Booking:
    route_app_labels ={'customer_data'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'customers_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'customers_db'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'customers_db'
        return None




