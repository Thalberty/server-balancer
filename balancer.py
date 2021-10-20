from typing import List


class ServerBalancer:

    def __init__(self, tasks_time: int, max_users: int):
        self.tasks_time = tasks_time
        self.max_users = max_users
        self.servers_historic = []
        self.servers = [[]]

    def server_balancer(self, new_users: List[int]):
        """Balance the number of servers.

        Server is an array of max length iqual to max_user, and each value in that
        list is the number of ticks remaning so the user is removed. When it gets
        to zero the user is removed.

        Servers is a list of servers.
        """
        # new_servers = [[]]
        for user_qnt in new_users:
            self.servers_in_tick(user_qnt)

        return self.servers_historic

    # def user_that_fits_in_a_server(server: list, max_users: int):
    #     if users < max_users and len(server) < users:

    def servers_in_tick(self, users_qnt):
        for server in self.servers:
            # user_for_server, next_users = user_that_fits_in_a_server(server)
            if users_qnt < self.max_users and len(server) < users_qnt:
                user_for_server = users_qnt \
                    if users_qnt <= self.max_users else users_qnt - self.max_users
                fits_in_server = user_for_server - len(server)
                # fits all users
                new_ticks = [self.tasks_time] * fits_in_server
                server.extend(new_ticks)

                if users_qnt > user_for_server:
                    pass  # repeat the process

                if users_qnt == 0:
                    continue  # next_ticket()

        num_servers = self.get_count_servers()
        self.servers_historic.append(num_servers)

        self.end_tick()

    def get_count_servers(self, servers):
        pass

    def end_tick(self):
        new_servers = []
        for server in self.servers:
            new_server = [tick-1 for tick in server]
            new_servers.append(new_server)

        self.servers = new_servers.copy()
