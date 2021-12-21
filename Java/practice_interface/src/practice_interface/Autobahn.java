package practice_interface;

public class Autobahn {
	public static void main(String[] args) {
		
		Car benz = new Car();
		
		int labTime = 10; 
		
		benz.start();
		
		for(int i=0; i<labTime; i++) {
			benz.drive();
		}
	
		benz.stop();		
		
	}
}
