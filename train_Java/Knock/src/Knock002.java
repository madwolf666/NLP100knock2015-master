/**
 * @author shin
 *
 */
public class Knock002 {

	public static void main(String[] args) {
		String tok1 = "パトカー"; 
		String tok2 = "タクシー"; 
		StringBuffer sb = new StringBuffer();
		
		for (int i=0; i<tok1.length(); i++){
			sb.append(tok1.charAt(i));
			sb.append(tok2.charAt(i));
		}
		System.out.println(sb.toString());
	}

}
