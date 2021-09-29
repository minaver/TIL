package practice_interface;

public class KumhoTire implements Tire{
	
	private int TireSpan = 3;
	
	@Override
	public void roll() {
		System.out.println("roll Kumho Tire!");
	}
	
	public int getTireSpan() {
		return TireSpan;
	}
}
