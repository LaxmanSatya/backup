# [TARGET AIM] ::: +1+

e_str : str = "Empolyee"
_parms : list = ["company", "id", "name", "designation", "salary", "experience"]

def take_data(parameter : str, type_ : type):
    if parameter.lower() in _parms:
            fvalue = type_(input(f'Enter {e_str} {parameter} : \033[95m'))
            print("\033[0m", end='')
            return fvalue
     
def inputer(parameter : str = "", type_ : type = str):
        try:
            if parameter != "" and parameter.lower() in _parms:
                return take_data(parameter, type_)
            else:
                _parms.append(parameter) # for the developer function.
                return take_data(parameter, type_)

        except ValueError as valueerror:
            print("Value Error Raised ::: Enter Correct TYPE Value")

        except TypeError as typeerror:
             print("Wrong Type of Data Entered!")
        
        except Exception as exception:
            print("Expection raised ::: %s"%(exception))

def empolyee_data():
        try:
            import pandas # type: ignore

            try:
                company = inputer("Company")
                id = inputer("ID")
                name = inputer("Name")
                designation = inputer("Designation")
                salary = inputer("Salary", int)
                year_of_experience = inputer("Experience")
                see_data : str = f''' \033[93m
                                {e_str} Currently Working Company \033[91m::: \033[94m{company}\033[93m
                                {e_str} ID                        \033[91m::: \033[94m{id}\033[93m
                                {e_str} Name                      \033[91m::: \033[94m{name}.\033[93m
                                {e_str} Designation               \033[91m::: \033[94m{designation}\033[93m.
                                {e_str} salary                    \033[91m::: \033[94m{salary}.00\033[93m
                                {e_str} experience                \033[91m::: \033[94m{year_of_experience} \033[0myears.
                                \033[0m
                            '''
                pandas.DataFrame([{
                    'company' : company,
                    'id' : id,
                    'name' : name,
                    'designation' : designation,
                    'salary' : salary,
                    'experience in years' : year_of_experience,
                }]).to_csv("Empolyee.csv", index = False)

                print("%s"%see_data)

            except Exception as exception:
                print("Expection raised ::: %s"%(exception))

        except Exception as exception:
            print("Expection raised ::: %s"%(exception))
        except KeyboardInterrupt as keyboardinterrupt:
            print("\033[96m!Exit.\033[0m")

if __name__ == '__main__':
     empolyee_data()