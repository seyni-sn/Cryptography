import java.awt.*;
import java.awt.image.*;
import javax.imageio.*;
import javax.swing.*;
import java.io.*;
import java.util.*;

public class LSB {

  // dissimuler une information secrete(du texte) dans une image
	public static BufferedImage dissimulerText(BufferedImage image, String text) {
		int bitMask = 0x00000001;	// definir le mask bit
		int bit;
		int x = 0;				// definir le pixel de depart x
		int y = 0;				// definir le pixel de depart  y
		for(int i = 0; i < text.length(); i++) {
			bit = (int) text.charAt(i);
			for(int j = 0; j < 8; j++) {
				int flag = bit & bitMask;
				if(flag == 1) {
					if(x < image.getWidth()) {
						image.setRGB(x, y, image.getRGB(x, y) | 0x00000001); 	// enregistrer le bit 1
						x++;
					}
					else {
						x = 0;
						y++;
						image.setRGB(x, y, image.getRGB(x, y) | 0x00000001); 	// enregistrer le bit 1
					}
				}
				else {
					if(x < image.getWidth()) {
						image.setRGB(x, y, image.getRGB(x, y) & 0xFFFFFFFE);	// enregistrer le bit 0
						x++;
					}
					else {
						x = 0;
						y++;
						image.setRGB(x, y, image.getRGB(x, y) & 0xFFFFFFFE);	// enregistrer le bit 0
					}
				}
				bit = bit >> 1;
			}
		}

		// savegarder l'image contenant l'information secret to dans une nouvelle image(imageAvecText)
		try {
			File outputfile = new File("imageAvecText.png");
			ImageIO.write(image, "png", outputfile);
		} catch (IOException e) {

		}
		return image;
	}

	// extraire l'information secret contenue dans l'image(imageAvecText)
	public static void extrairText(BufferedImage image, int length) {
		System.out.print("Extraction du text: ");
		int bitMask = 0x00000001;
		int x = 0;
		int y = 0;
		int flag;
		char[] c = new char[length] ;	// definir le tableau de charactere qui va contenir l'information secrete
		for(int i = 0; i < length; i++) {
			int bit = 0;


			for(int j = 0; j < 8; j++) {
				if(x < image.getWidth()) {
					flag = image.getRGB(x, y) & bitMask;
					x++;
				}
				else {
					x = 0;
					y++;
					flag = image.getRGB(x, y) & bitMask;
				}

				if(flag == 1) {
					bit = bit >> 1;
					bit = bit | 0x80;
				}
				else {
					bit = bit >> 1;
				}
			}
			c[i] = (char) bit;
			System.out.print(c[i]);
		}
	}
//On dissimul en ensuite on extrait
//######################################################
// dissimuler une information secrete(du texte) dans une image

//########################################################
// extraire l'information secret contenue dans l'image(imageAvecText)

	public static void main(String[] args) {

		BufferedImage originalImageText = null;
		BufferedImage dissimulImageText = null;
		BufferedImage originalImage = null;
		BufferedImage coverImage = null;
		BufferedImage secretImage = null;

		// afficher une interface utilisateur avec l'image d'origine et l'image de contenant l'information secrete
		try {
			originalImageText = ImageIO.read(new File("cover.jpg"));
			dissimulImageText = ImageIO.read(new File("cover.jpg"));

			String chaine;
			Scanner scan = new Scanner(System.in);
			System.out.print("Donner le text a dissimuler: ");
			chaine = scan.nextLine();
			dissimulImageText = dissimulerText(dissimulImageText, chaine);								// dissimuler   l'information secret
			extrairText(ImageIO.read(new File("imageAvecText.png")), chaine.length());		// extraire l'information secret
			JFrame frame = new JFrame("Text Steganography");
			JPanel panel = new JPanel();
			JLabel label1 = new JLabel(new ImageIcon(originalImageText));
			JLabel label2 = new JLabel(new ImageIcon(dissimulImageText));
			panel.add(label1);
			panel.add(label2);
			frame.add(panel);
			frame.pack();
			frame.setVisible(true);


		} catch(IOException e) {

		}
	}
}
