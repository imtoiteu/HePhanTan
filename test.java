import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;

public class test {
    public static void main(String[] args) {
        // Khởi tạo một đối tượng PasswordEncoder
        BCryptPasswordEncoder passwordEncoder = new BCryptPasswordEncoder();

        // Tạo user với username là "imtoiteu" và password là "123"
        String username = "imtoiteu";
        String password = "123";

        // Mã hóa password
        String hashedPassword = passwordEncoder.encode(password);

        // In ra màn hình username và password đã được mã hóa
        System.out.println("Username: " + username);
        System.out.println("Password: " + hashedPassword);
    }
}
