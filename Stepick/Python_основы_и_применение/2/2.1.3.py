class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, object):
        if object > 0:
            return super().append(object)
        else:
            raise NonPositiveError


my_list = PositiveList()

my_list.append(-3)
