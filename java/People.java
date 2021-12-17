// Example 5: People.java

record FullName(String name) {
    FullName {
        System.out.println("FullName checking " + name);
        Check.validity(name.split(" ").length > 1,
                name + " needs at least first and last names");
    }
}

record BirthDate(String dob) {
    BirthDate {
        System.out.println("BirthDate checking " + dob);
        Check.validity(true, "Add code to validate " + dob);
    }
}

record EmailAddress(String address) {
    EmailAddress {
        System.out.println("EmailAddress checking " + address);
        Check.validity(true, "Add code to validate" + address);
    }
}

record Person(FullName name, BirthDate dateOfBirth, EmailAddress email) {
    Person {
        System.out.println("Person checking fields");
        Check.validity(true, "Add code to validate Person");
    }
}

public class People {
    public static void main(String[] args) {
        var person = new Person(
            new FullName("Bruce Eckel"),
            new BirthDate("7/8/1957"),
            new EmailAddress("mindviewinc@gmail.com")
        );
    }
}
