package second_package;

import java_practice.Class_test1;
import java_practice.Class_test2;

public class Class_test3 {
	public static void main(String args[]) {
		Class_test1 test1 = new Class_test1();
		Class_test2 test2 = new Class_test2("ryan",6000,"back-end");
		
		//System.out.println(test2.name); // The field Class_test1.name is not visible <- name은 protected이므로 다른 모듈에서 사용불가 / getter 사용하여 name 접
		System.out.println(test2.getName()); // getter의 사용 
	}
}

