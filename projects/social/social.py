# average number of friendships is exactly 2 but the actual number of friends per user ranges anywhere from 0 to 4.

import random


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.friendships[vertex_id]

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(1, num_users + 1):
            self.add_user(i)
        # Create friendships
        listed_users = []
        all_possible_friendships = []
        for user in self.users:
            listed_users.append(user)
        counter = 0
        for i in range(1, len(listed_users) + 1):
            for j in range(i + 1, len(listed_users) + 1):
                all_possible_friendships.append((i, j))

        random.shuffle(all_possible_friendships)

        num_friendships = (num_users * avg_friendships) // 2
        for i in range(0, num_friendships):
            friendship = all_possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """

        q = Queue()
        q.enqueue([user_id])
        visited = {}  # Note that this is a dictionary, not a set

        # """reset friendships for test purposes"""
        # self.friendships = {1: {4, 5}, 2: {9, 5}, 3: {8}, 4: {8, 1}, 5: {1, 2, 6, 7}, 6: {5, 7}, 7: {8, 5, 6}, 8: {3, 4, 7}, 9: {2}, 10: set()}


        # !!!! IMPLEMENT ME

        while q.size() > 0:
            path = q.dequeue()
            node = path[-1]

            if node not in visited:
                neighbors = self.get_neighbors(node)

                for neighbor in neighbors:
                    new_path = list(path)
                    new_path.append(neighbor)
                    q.enqueue(new_path)
                visited[node] = path

        return visited



if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    connections = sg.get_all_social_paths(1)
    print(sg.friendships)
    print(connections)
