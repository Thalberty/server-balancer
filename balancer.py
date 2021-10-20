from typing import List


class ServerBalancer:

    def __init__(self, tasks_time: int, max_users: int):
        self.tasks_time = tasks_time
        self.max_users = max_users
        self.servers_historic = []
        self.servers = [[]]

    def server_balancer(self, new_users: List[int]):
        """Balance the number of servers.

        Server is an array of max length iqual to max_user, and each value in
        that list is the number of ticks remaning so the user is removed. When
        it gets to zero the user is removed.

        Servers is a list of servers.
        """
        # new_servers = [[]]
        for user_qnt in new_users:
            self.servers_in_tick(user_qnt)

            num_servers = self.get_count_servers()
            self.servers_historic.append(num_servers)

            self.end_tick()

        return self.servers_historic

    def servers_in_tick(self, users_qnt):
        for server in self.servers:
            users_remaing = users_qnt.copy()
            while users_remaing:
                user_for_server = self.get_user_for_server(users_remaing)
                server = self.add_user_in_server(user_for_server, server)
                users_remaing = users_remaing - user_for_server

    def get_user_for_server(self, users_qnt):
        if users_qnt <= self.max_users:
            return users_qnt
        else:
            return users_qnt - self.max_users

    def add_user_in_server(self, user_for_server, server=[]):

        fits_in_server = user_for_server - len(server)
        new_ticks = [self.tasks_time] * fits_in_server
        server.extend(new_ticks)

        return server

    def get_count_servers(self, servers):
        pass

    def end_tick(self):
        new_servers = []
        for server in self.servers:
            new_server = [tick-1 for tick in server]
            new_servers.append(new_server)

        self.servers = new_servers.copy()
