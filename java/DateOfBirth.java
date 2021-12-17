// Example 6: DateOfBirth.java

record Day(int day) {
    Day {
        Check.validity(0 < day && day <= 31, day + ": day of month out of range");
    }
}

record Month(int month) {
    Month {
        Check.validity(0 < month && month <= 12, month + ": month out of range");
    }
}

record Year(int year) {
    Year {
        Check.validity(1900 < year && year <= 2022, year + ": year out of range");
    }
}

record BirthDate(Month m, Day d, Year y) {}

public class DateOfBirth {
    public static void main(String[] args) {
        System.out.println(new BirthDate(new Month(7), new Day(8), new Year(1957)));
        System.out.println(new BirthDate(new Month(0), new Day(32), new Year(1857)));
    }
}
