package practice_interface;

public class HankookTire implements Tire {
	
	private int TireSpan = 5;
	
	@Override
	public void roll() { // Tire's roll() function is public so implemented class only can get public
		System.out.println("roll Hankook Tire!");
	}
	
	public int getTireSpan() {
		return TireSpan;
	}
}
