package practice_thread;

public class ClassAnonyRunnable {
	public static void main(String[] args) {
		
		Thread t1 = new Thread(new Runnable() {
			@Override
			public void run() {
				try {
					Thread.sleep(1000);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				System.out.println("Thread name : "+Thread.currentThread().getName()+" || Thread ID : "+ Thread.currentThread().getId());
			}
		});
		
		 new Thread(new Runnable() {
			@Override
			public void run() {
				try {
					Thread.sleep(1000);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				System.out.println("No reuse Thread name : "+Thread.currentThread().getName()+" || Thread ID : "+ Thread.currentThread().getId());
			}
		}).start();
		
		System.out.println("Am i first one?");
		
		t1.start();
//		try {
//			t1.join();
//		} catch (InterruptedException e) {
//			// TODO Auto-generated catch block
//			e.printStackTrace();
//		}
		
		
	}
}
