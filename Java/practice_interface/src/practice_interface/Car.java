package practice_interface;

public class Car {
	
	Tire fl = new HankookTire();
	Tire fr = new HankookTire();
	Tire bl = new KumhoTire();
	Tire br = new KumhoTire();
	
	int fl_span = fl.getTireSpan();
	int fr_span = fr.getTireSpan();
	int bl_span = bl.getTireSpan();
	int br_span = br.getTireSpan();
	
	int fl_count =0;
	int fr_count =0;
	int bl_count =0;
	int br_count =0;
	
	public void start() {
		fl.roll();
		fr.roll();
		bl.roll();
		br.roll();
	}
	
	public void stop() {
		System.out.println("fl_count : "+fl_count);
		System.out.println("fr_count : "+fr_count);
		System.out.println("bl_count : "+bl_count);
		System.out.println("br_count : "+br_count);

	}
	
	public void drive() {
		try {
			Thread.sleep(1000);
			System.out.println("[ spend 1 second ]");
			useTire();
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}
	
	public void useTire() {
		if((fl_span -= 1) == 0) {
			fl_span = fl.getTireSpan();
			System.out.println("Change fl Tire!");
			fl_count++;
		}
		if((fr_span -= 1) == 0) {
			fr_span = fr.getTireSpan();
			System.out.println("Change fr Tire!");
			fr_count++;
		}
		if((bl_span -= 1) == 0) {
			bl_span = bl.getTireSpan();
			System.out.println("Change bl Tire!");
			bl_count++;
		}
		if((br_span -= 1) == 0) {
			br_span = br.getTireSpan();
			System.out.println("Change br Tire!");
			br_count++;
		}
	}
	

}
