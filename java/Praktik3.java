import java.util.Scanner;

public class Praktik3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean isRunning = true;

        while (isRunning) {
            System.out.print("Masukkan lantai tujuan (0 untuk keluar): ");
            int floor = scanner.nextInt();

            if (floor == 0) {
                System.out.println("Terima kasih telah menggunakan lift.");
                isRunning = false;
            } else if (floor == 13) {
                System.out.println("Lantai 13 tidak tersedia.");
            } else if (floor > 13) {
                System.out.println("Lift berada di lantai: " + (floor - 1));
            } else {
                System.out.println("Lift berada di lantai: " + floor);
            }
        }

        scanner.close();
        System.out.println("Nama : Muhammad Haidar JIhad Izzuddin");
        System.out.println("NIM : 0110222205");
        System.out.println("TI09");
    }
}