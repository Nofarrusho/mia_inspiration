def main_menu():
    while True:
        print("\n=== מערכת ניהול ארגונית ===")
        print("1. שירות לקוחות")
        print("2. ניהול מחסן")
        print("3. יציאה")
        choice = input("בחר אפשרות: ")

        if choice == "1":
            customer_service_menu()
        elif choice == "2":
            warehouse_menu()
        elif choice == "3":
            print("להתראות!")
            break
        else:
            print("בחירה לא חוקית. נסה שוב.")

def customer_service_menu():
    while True:
        print("\n--- שירות לקוחות ---")
        print("1. לקוח - הגש פנייה")
        print("2. נציג שירות - ניהול פניות")
        print("3. חזרה לתפריט הראשי")
        choice = input("בחר אפשרות: ")

        if choice == "1":
            create_customer_inquiry()
        elif choice == "2":
            agent_menu()
        elif choice == "3":
            break
        else:
            print("בחירה לא חוקית. נסה שוב.")

def warehouse_menu():
    while True:
        print("\n--- ניהול מחסן ---")
        print("1. סריקת מלאי")
        print("2. עדכון מלאי")
        print("3. הצגת הזמנות")
        print("4. חזרה לתפריט הראשי")
        choice = input("בחר אפשרות: ")

        if choice == "1":
            print("סריקה בוצעה!")
        elif choice == "2":
            print("מלאי עודכן.")
        elif choice == "3":
            print("רשימת הזמנות מוצגת.")
        elif choice == "4":
            break
        else:
            print("בחירה לא חוקית. נסה שוב.")

def create_customer_inquiry():
    print("\n--- לקוח - הגשת פנייה ---")
    name = input("שם: ")
    email = input("אימייל: ")
    phone = input("טלפון: ")
    description = input("תיאור הפנייה: ")

    # כאן תוסיפי את הקוד שמכניס את הפנייה לבסיס הנתונים או קורא למחלקה
    print(f"\nפנייה נוצרה עבור {name}. תודה על פנייתך!")

def agent_menu():
    while True:
        print("\n--- נציג שירות - ניהול פניות ---")
        print("1. הצגת פניות")
        print("2. עדכון סטטוס פנייה")
        print("3. חזרה לתפריט הקודם")
        choice = input("בחר אפשרות: ")

        if choice == "1":
            print("מציג את כל הפניות...")
        elif choice == "2":
            inquiry_id = input("הזן מזהה פנייה: ")
            new_status = input("הזן סטטוס חדש: ")
            print(f"סטטוס הפנייה {inquiry_id} עודכן ל-{new_status}.")
        elif choice == "3":
            break
        else:
            print("בחירה לא חוקית. נסה שוב.")

if __name__ == '__main__':
    main_menu()
