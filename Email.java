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

        }
    }
}
