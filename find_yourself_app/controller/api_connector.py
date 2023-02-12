from controller.read_configs import read_json_config


class Authorization:
    @staticmethod
    def authorization(user, password):
        config = read_json_config()
        if user == config['flask']['username'] and password == config['flask']['password']:
            return True
        return False
