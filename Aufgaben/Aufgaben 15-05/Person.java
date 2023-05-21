import java.util.Scanner;

public class Person {
    private String name;
    private String date;
    private static Person instance;

    private Person(String name, String date) {
        this.name = name;
        this.date = date;
    }

    public static Person getInstance() {
        if (instance == null) {
            synchronized (Person.class) {
                if (instance == null) {
                    createInstance();
                }
            }
        }
        return instance;
    }

    private static void createInstance() {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Name eingeben: ");
        String name = scanner.nextLine();

        System.out.print("Datum eingeben: ");
        String date = scanner.nextLine();

        instance = new Person(name, date);
        scanner.close();
        System.out.println("Name: "+name);
        System.out.println("Datum: "+date);
    }

    public String getName() {
        return name;
    }

    public String getDate() {
        return date;
    }
}
