class Voting:

    def __init__(self):
        print("Working in Voting special method or constructor")
        self.students = {0: {"name": "James", "v_mark": 0, "voter": []},
                         1: {"name": "John", "v_mark": 0, "voter": []},
                         2: {"name": "Rooney", "v_mark": 0, "voter": []},
                         3: {"name": "Ronaldo", "v_mark": 0, "voter": []},
                         4: {"name": "Messi", "v_mark": 0, "voter": []}
                         }
        self.db: dict = {}
        self.id: int= 0
        self.l_id: int = 0
        self.r_total: int = 2000



    def main_option(self):
        option = 0
        try:
            option = int(input("Press 1 to register\nPress 2 to login\nPress 3 to exit"))

        except Exception as err:
            print(err)

        if option == 1:
            self.register()
        elif option == 2:
            self.login()
        elif option == 3:
            self.exit()
        else:
            print("Invalid Option.Please select an Integer eg.1,2,3")
            self.main_option()




    def register(self):
        print("This is Registration Section")
        try:
            r_email = input("Enter your email to register :")
            r_name = input("Enter your name to register :")
            r_pass = input("Enter your password to register :")
            r_pass2 = input("Retype password :")

            if r_pass2 != r_pass:
                print("Password doesnt match")
                self.main_option()
                return


        except Exception as err:
            print(err)

        self.id = len(self.db)
        r_total = 2000
        data_form: dict = {self.id: {"email": r_email, "name": r_name, "pass": r_pass,"total": r_total}}

        self.db.update(data_form)
        print("Registration successful,", self.db[self.id]["name"],"$",self.db[self.id]["total"])


        while True:
            r_option = input("Press 1 to login:\nPress 2 to Main Option\nPress 3 to exit")
            try:
                r_option = int(r_option)
                if r_option == 1:
                    self.login()
                    break
                elif r_option == 2:
                    print("Main Option")
                    self.main_option()
                    break
                elif r_option == 3:
                    exit(1)
                else:
                    print("Invalid Input.Please follow the description eg.1,2,3")

            except Exception as err:
                print(err)
    def login(self):
        print("This is login sector")
        length = len(self.db)
        try:
            l_email = input("Enter your email to login:")
            l_pass = input("Enter your password to login:")
            self.l_id = -1

            for i in range(length):
                if l_email == self.db[i]["email"] and l_pass == self.db[i]["pass"]:

                    self.l_id = i
                    break
            if self.l_id != -1:
                self.user_sector(self.l_id)
                return

            else:
                print("Username or Password Incorrect")
                self.login()

        except Exception as err:
            print(err,"\nInvalid Input:")

    def user_sector(self, user_id):
        print("Welcome", self.db[user_id]["name"] , self.db[self.l_id]["total"])
        self.db[self.l_id][self.r_total] = 2000

        print("Please select one!")
        print("1 Vote is equal to $500")
        for i in range(len(self.students)):
            print("Id:{} - Name {} - Current Vote Mark: {}".format(i, self.students[i]["name"],self.students[i]["v_mark"]))

        try:
            v_id = int(input("Just Enter Id number to vote:"))

            self.students[v_id]["v_mark"] += 1

            self.students[v_id]["voter"].append(self.db[self.l_id]["name"])

            print("Congratulations you have voted!")

            print("{} 's voting mark is now : {}".format(self.students[v_id]["name"], self.students[v_id]["v_mark"]))
            self.rip_money()
            self.save_data()

            for i in range(len(self.students[v_id]["voter"])):
                print("Voter: ", self.students[v_id]["voter"][i])
        except Exception as err:
            print(err)

        while True:
            if self.db[self.l_id]["total"] != 0:
                try:
                    vote_option = int(input("Press 1 to Vote Again!\nPress 2 to get to Main Option!\nPress 3 to Force Quit:"))

                    if vote_option == 1:
                        self.user_sector(self.l_id)
                        break
                    elif vote_option == 2:
                        self.main_option()
                        break
                    elif vote_option == 3:
                        exit(1)
                    else:
                        print("Invalid option after vote!")
                except Exception as err:
                    print(err)
            else:
                print("You have used all of your money")
                bp = int(input("Press 1 to buy Points\nPress 2 to vote again\nPress 3 to Main Option"))
            try:
                if bp == 1:
                    self.buy_money()
                elif bp == 2:
                    self.user_sector(self.l_id)
                elif bp == 3:
                    self.main_option()
                else:
                    print("Choose a Valid option")
            except  Exception as err:
                print(err)



    def save_data(self):
        with open("all_data.txt", "w") as file:
            file.write("[Registered Users]\n")
            for user_id, user_data in self.db.items():
                line = f"{user_id},{user_data['email']},{user_data['name']},{user_data['pass']}\n"
                file.write(line)

            file.write("\n[Student Voters]\n")
            for student_id, student_data in self.students.items():
                line = f"{student_id},{student_data['name']},{student_data['v_mark']},{student_data['voter']}\n"
                file.write(line)

        print("Saved.")

    def rip_money(self):
        self.db[self.l_id]["total"] -= 500
        print("Your total is now:", self.db[self.l_id]["total"])

    def buy_money(self):
        buying = int(input("Press 1 to buy One Point"))

        try:
            if buying == 1:
                self.db[self.l_id]["total"] += 500
        except Exception as err:
            print(err)

        print(self.db[self.l_id]["name"] , "Your balance is now :" , self.db[self.l_id]["total"])
        after_buying = int(input("Press 1 to buy More Points\nPress 2 to vote\nPress 3 to Main Option"))
        try:
            if after_buying == 1:
                self.buy_money()
            elif after_buying == 2:
                self.user_sector(self.l_id)
            elif after_buying == 3:
                self.main_option()
        except Exception as err:
            print(err)


if __name__ == '__main__':
    voting = Voting()
    voting.main_option()




















