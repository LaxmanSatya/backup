public class CommonStringMethodsDemo {
    public static void main(String[] args) {
        String text = "       \n          Learning programing is different from learning programs  ";
        System.out.println("Original or Given string : " + text); 

        // 1. length(): Count of characters
        System.out.println("Length: " + text.length()); 

        // 2. trim(): Removes leading and trailing whitespace
        String cleanText = text.trim();
        System.out.println("Trimmed: " + cleanText); /// [NOW]

        // 3. charAt(index): Returns character at specified position
        System.out.println("Char at index 0: " + cleanText.charAt(0)); 
	
	// 4. indexOf(string): Returns first occurrence of the given string
        System.out.println("First occurrence Index of 'program': " + cleanText.indexOf("program")); 
	
	// 5. lastIndexOf(string): Returns last occurrence of the given string
        System.out.println("Last occurrence Index of 'program': " + cleanText.lastIndexOf("program"));
        
	// 6. substring(start, end): Extracts a portion of text
        System.out.println("Substring (0 to 5): " + cleanText.substring(0, 5)); 

        // 7. toUpperCase() & toLowerCase()
        System.out.println("Upper: " + cleanText.toUpperCase()); 
	System.out.println("Lower: " + cleanText.toLowerCase());

        // 8. contains() & startsWith()
        System.out.println("Contains 'programs'? " + cleanText.contains("programs")); 
        System.out.println("Starts with 'Learning'? " + cleanText.startsWith("Learning")); 

        // 9. replace(old, new)
        System.out.println("Replaced: " + cleanText.replace("programing", "programming")); 
    }
}
