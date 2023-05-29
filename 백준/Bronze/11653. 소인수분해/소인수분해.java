import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int num = Integer.parseInt(br.readLine());
		while (num != 1) {
			if (num == 1) {
				break;
			}
			for (int i=2; i<10000000; i++) {
				if (num % i == 0) {
					num = num / i;
					System.out.println(i);
					break;
				}		
			}
		}
	}
}