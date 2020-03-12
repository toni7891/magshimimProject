from collections import OrderedDict


def main():
  user_input_str = input("Enter an shop list[item,item,item]: ")
  user_input_str = user_input_str.split(",")
  menu(user_input_str)


def menu(user_list):
  """
  Prints the menu for interactions with the list user entered.
  :param user_list: The list the user entered.
  :return: None
  """
  user_choose = 0
  while not user_choose == 9:
    user_choose = int(input("""\t1: Print the list.
    2: Print the number of item's in the list.
    3: Check if item in list.
    4: Check how many times item appear in the list?
    5: Remove item from list. (*only one appearance of the item will be removed from the list*)
    6: Add item to the list.
    7: Print invalid item's.
    8: Remove repeating item's from list.
    9: Exit
    """))

    if user_choose == 1:
      print_list(user_list)

    elif user_choose == 2:
      print_num_items(user_list)

    elif user_choose == 3:
      item_to_check = input("Enter the item to search in list: ")
      check_item_in(item_to_check, user_list)

    elif user_choose == 4:
      item_to_many = input("Enter the item to count appearance in list: ")
      how_many_apperience(item_to_many, user_list)

    elif user_choose == 5:
      item_to_many = input("Enter the item to remove from the list: ")
      remove_item_from(item_to_many, user_list)

    elif user_choose == 6:
      item_to_add = input("Enter the item to add to the list: ")
      add_item_to(item_to_add, user_list)

    elif user_choose == 7:
      not_alpha_chars(user_list)

    elif user_choose == 8:
      dupli_remover(user_list)

    elif user_choose == 9:
      print("Good bye!")
      break


def print_list(user_list):
  """
  Print list.
  :param user_list: The given list.
  :return: The list
  """
  print(user_list)
  return user_list


def print_num_items(user_list):
  """
  Prints number of item's in the list.
  :param user_list:
  :return:
  """
  print(len(user_list))


def check_item_in(item, user_list):
  if item in user_list:
    print("The searched item: ", item, ", exist in the list!")
  else:
    print("The item: ", item, ", dosen't exist in the list!")


def how_many_apperience(item, user_list):
  how_many = user_list.count(item)
  print("The item: ", item, "apper's in the list", how_many, "time's!")


def remove_item_from(item, user_list):
  user_list.remove(item)
  print("Item removed!")
  print("the list after the remove of ", item, ":", user_list)


def add_item_to(item, user_list):

  user_list.append(item)
  print("the list after adding the item: ", user_list)


def not_alpha_chars(user_list):
  new_list = []
  flag = 0
  for item in user_list:
    if item.isalpha() == 0 or len(item) < 3:
      flag += 1
      new_list += [item]

  if flag > 0:
    print("All invalid item's: ", new_list)

  elif flag == 0:
    print("All of the item's are valid!")


def dupli_remover(user_list):
  user_list = list(dict.fromkeys(user_list))
  print(user_list)


if __name__ == "__main__":
  main()
