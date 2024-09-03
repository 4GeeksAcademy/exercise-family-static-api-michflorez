from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {
                "id": 1,
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22],
            },
            {
                "id": 2,
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3],
            },
            {
                "id": 3,
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers": [1],
            },
        ]

    def _generate_id(self):
      return randint(0,999999)

    def add_member(self, member):
        current_members = self._members[:]

        if not all(key in member for key in ("first_name", "age", "lucky_numbers")):
            raise ValueError("Missing fields in member data")
        
        if "id" not in member:  
            member["id"] = self._generate_id()

        member["last_name"] = self.last_name
        member["id"] = int(member["id"])
        member["age"] = int(member["age"])
        member["lucky_numbers"] = list(member["lucky_numbers"])

        new_member = {
            "id": member["id"],
            "first_name": member["first_name"],
            "last_name": member["last_name"],
            "age": member["age"],
            "lucky_numbers": member["lucky_numbers"],
        }    

        current_members.append(new_member)
        self._members = current_members

    def delete_member(self, id):
        self._members = [member for member in self._members if member["id"] != id]

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
        return None

    def get_all_members(self):
        return self._members
