package prac_protected;

import java_practice.*;

public class Class_test3 { // practice can't use protected field so use getter
	
	public static void main(String args[]) {
		Class_test2 test2 = new Class_test2("ryan",6000,"back-end");
		
		//System.out.println(test2.name); // The field Class_test1.name is not visible <- name은 protected이므로 다른 모듈에서 사용불가 / getter 사용하여 name 접근 
		System.out.println(test2.getName()); // getter의 사용 
	}
}

