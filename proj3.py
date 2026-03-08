import json
file_name="To_do_list.json"
def load_tasks():

    try:
        with open(file_name,"r") as file:
            return json.load(file)
    except:
        return{"tasks":[]}
    def save_tasks(tasks):
        try:
           with open(file_name,"r") as file:
                return json.dump(tasks,file)
        except:
            print("failed to save.")
            def view_tasks(task):
                print()
                task_list=tasks["tasks"]
                if len(task_list)==0:
                    print("No tasks to display.")
                else:
                    print("Yourto do list:")
                    for idx, tasks in enumerate(task_list):
                        status="[completed]" if task["complete"]else "[pending]"
                        print(f"{idx+1}.{task['description']})|{status}")
                        def create_task(tasks):
                            description=input("enter the task description:").strip()
                            if description:
                                tasks["tasks"].append({"description":description,"complete":False})
                                save_tasks(tasks)
                                print("Task added.")
                            else:
                                print("Description cannot be empty.")
                                def mark_task_complete(tasks):
                                    view_tasks(tasks)
                                    try:
                                        task_number=int(input("enter the task number to mark for complete:").strip())
                                        if 1<=task_number<=len(tasks):
                                            tasks["tasks"][task_number-1]["complete"]=True
                                            save_tasks(tasks)
                                            print("task marked as complete.")
                                        else:
                                            print("invlaid task number.")
                                    except:
                                        print("enter a valid number.")
                                        def main():
                                            tasks=load_tasks()
                                            while True:
                                                print("\nto Do list manager")
                                                print("1.view tasks")
                                                print("2.add tasks")
                                                print("3.complete task")
                                                print("4.exit")

                                                choice=input("Enter your choice:").strip()
                                                if choice=="1":
                                                    view_tasks(tasks)
                                                elif choice=="2":
                                                    create_task(tasks)
                                                elif choice=="3":
                                                    mark_task_complete(tasks)
                                                elif choice=="4":
                                                    print("Goodbye")
                                                    break
                                                else:
                                                    print("Invalid choice.please try again.")


                                    






