import java.util.*;
public class Email {

    public static void main(String[] args){
        System.out.println("-------------------------------");
        System.out.println("1: Make an email and password");
        System.out.println("2: Change password");
        System.out.println("3: Show your email and password");
        System.out.println("-------------------------------");

        Scanner scan = new Scanner(System.in);
        System.out.println("Write the option you would like: ");
        String userChoice = scan.nextLine();

        if (userChoice.equals("1")){
            System.out.println("Please write your name");
            String userName = scan.nextLine();
            System.out.println(userName);

            System.out.println("Please write your surname: ");
            String userSurname = scan.nextLine();
            System.out.println(userSurname);

            System.out.println("Please write the department you work in: ");
            String userDepartment = scan.nextLine();
            System.out.println(userDepartment);

            String gmail = "@gmail.com";
            String outlook = "@outlook.com";
            String yahoo = "@yahoo.com";
            String icloud = "@iCloud";

            System.out.println("--------------");
            System.out.println("1: " + gmail);
            System.out.println("2: " + outlook);
            System.out.println("3: " + yahoo);
            System.out.println("4: " + icloud);
            System.out.println("---------------");

            System.out.println("Please pick the ending of your email you would like: ");
            String emailPick = scan.nextLine();
            if (emailPick.equals("1")) {
                String finalEmail = userName + userSurname + userDepartment + gmail;
                System.out.println("This is your new email: " + finalEmail);
            } else if (emailPick.equals("2")) {
                String finalEmail = userName + userSurname + userDepartment + outlook;
                System.out.println("This is your new email: " + finalEmail);
            } else if (emailPick.equals("3")) {
                String finalEmail = userName + userSurname + userDepartment + yahoo;
                System.out.println("This is your new email: " + finalEmail);
            } else if (emailPick.equals("4")) {
                String finalEmail = userName + userSurname + userDepartment + icloud;
                System.out.println("This is your new email: " + finalEmail);
            }
        }
    }
}
