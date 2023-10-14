/*
 * 
Morgan State University
Department of Electrical & Computer Engineering
EEGR 415: Java Programing Applications
Project 2.1
Objective:
Transform Project 1 into a full-fledged GUI application for the classification of fruit feature data.
Create the graphical user interface
Create a graphical user interface for project 1 as follows:
The file menu has the following options:
The view menu only has one menu option, which is a check box that is checked by default.
The combo box under (View Data Samples) has the following:
Hints:
• To get the text in the frames around each main panel, use TitledBorder (Google it)
• You should add your Menu bar object to your Frame object using the method setJMenuBar (add
it before you make the frame visible)
 */
import java.io.*;
import java.util.Scanner;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.GroupLayout.Alignment;
import chapman.graphics.JPlot2D;
import chapman.graphics.Plot2D;
import javax.swing.border.TitledBorder;
public class Project2 extends JPanel {
    //booleans
    public static boolean one_point;
    public static boolean many_points;
    //integers
    public static int arrays;
    public static int index;
    public static int index2;
    public static int MAX_SAMPLES;
    public static int I;
    public static int counter;
    //doubles
    public static double single_point_value;
    public static double multiple_point_value;
    //JPanel Class Objects
    public static JTextField x1_entered;
    public static JTextField x2_entered;
    public static JRadioButton single_point;
    public static JRadioButton multiple_points;
    public static ButtonGroup button_group;
    public static JLabel Feature;
    public static JLabel Training;
    public static JLabel trained_weights_text;
    public static JLabel feature_1_text_label;
    public static JLabel feature_2_text_label;
    public static JCheckBox show_training;
    public static JCheckBox show_decision_boundary_line;
    private static JButton train;
    private static JButton test;
    //2D arrays
    public static double[][] tcData;
    public static double[][] fcData;
    public static String view_selection;
    public static String view_str;
    //1D arrays
    public static double[] X1_true;
    public static double[] X2_true;
    public static double[] X1_false;
    public static double[] X2_false;
    public static double[] w;
    public static double[] Entered_X1;
    public static double[] Entered_X2;
    public static double[] x;
    public static double[] y;
    public static double[] y_w;
    //Arrays JComponents
    public static JLabel[] JLabel_Array;
    public static JTextField[] JTextField_Array;
    //Text Areas
    public static JTextArea X1;
    public static JTextArea X2;
    public static JTextArea data_txt;
    public static JTextArea testing;
    public static JTextArea bias;
    public static JTextArea feature1;
    public static JTextArea feature2;
    //Frame for plot
    public static JFrame frame_plot;
    //Plot
    public static JPlot2D plot1;
    //JPanels
    public static JPanel panel_plot;
    public static JPanel panel_main;
    public static JPanel panel_ViewDataSamples;
    public static JPanel panel_TrainedWeights;
    public static JPanel panel_Testing;
    public static JPanel right_panel;
    public static JPanel bottom_right_panel;
    public static JPanel testing_panel_text;
    public static JPanel testing_panel_buttons;
    public static void main(String[] args)throws IOException {
    JFrame frame = new JFrame("Project 2");
    w = new double[3];
    y_w = new double[w.length];
    I = 100;
    MAX_SAMPLES = 10;
    tcData = new double[MAX_SAMPLES][2];
    fcData = new double[MAX_SAMPLES][2];
    X1_true = new double[MAX_SAMPLES];
    X2_true = new double[MAX_SAMPLES];
    X1_false = new double[MAX_SAMPLES];
    X2_false = new double[MAX_SAMPLES];
    view_selection = new String();
    data_txt = new JTextArea();
    testing = new JTextArea();
    testing.setText("Bias \t\t\t Feature 1 \t\t\t Feature 2 \n"
    + "0 \t\t\t 0 \t\t\t 0");
    testing.setPreferredSize(new Dimension(900,1000));
    one_point = true;
    many_points = false;
    X1 = new JTextArea("");
    X2 = new JTextArea("");
    File DataFile = new File("data.txt");
    Scanner in = new Scanner(DataFile);
    //Populating 2D arrays
    for(index2 = 0; index2 <= 1; index2++) {
        for(index = 0; index < MAX_SAMPLES; index++) {
        tcData[index][index2] = in.nextDouble();
        }
    }
    for(index2 = 0; index2 <= 1; index2++) {
        for(index = 0; index < MAX_SAMPLES; index++) {
        fcData[index][index2] = in.nextDouble();
        }
    }
//Populating 1D arrays from 2D arrays
    for(index = 0; index < 20; index++) {
        if(index < MAX_SAMPLES) {
            X1_true[index] = tcData[index][0];
            X2_true[index] = tcData[index][1];
        }
        else {
            X1_false[index-MAX_SAMPLES] = fcData[index-MAX_SAMPLES][0];
            X2_false[index-MAX_SAMPLES] = fcData[index-MAX_SAMPLES][1];
        }
    }
    for (int i = 1; i < I; i++){
        for (int n = 0; n < MAX_SAMPLES; n++){
        //Weight adjusting for case 1
            if ((w[0] * 1) + (w[1] * X1_true[n] + (w[2] * X2_true[n]))
            < 0){
                w[0] = w[0] + 1;
                w[1] = w[1] + X1_true[n];
                w[2] = w[2] + X2_true[n];
            }
            //Weight adjusting for case 2
            if ((w[0] * 1) + (w[1] * X1_false[n] + (w[2] *
            X2_false[n])) >= 0){
                w[0] = w[0] - 1;
                w[1] = w[1] - X1_false[n];
                w[2] = w[2] - X2_false[n];
            }
        }
    }
    System.out.print("X1(True)" + "\t" + "X2(True)" + "\t" + "X1(False)" +
    "\t" + "X2(False)" + "\n");
    System.out.print("--------" + "\t" + "--------" + "\t" + "--------" +
    "\t" + "--------" + "\n");
    for(index = 0; index < MAX_SAMPLES; index++) {
        for(arrays = 1; arrays <= 2; arrays++) {
            for(index2 = 0; index2<=1; index2++) {
                switch(arrays) {
                    case 1:
                    System.out.print(tcData[index][index2] + "\t");
                    break;
                    case 2:
                    System.out.print(fcData[index][index2] + "\t");
                    break;
            }
            System.out.print("\t");
            }
        }
        System.out.print("\n");
    }
    //y = (w0 + x(w1))/-w2
    x = new double[5];
    y = new double[5];
    for (index = 0; index < 5; index++){
        x[index] = index + 5;
        y[index] = (w[0] + (x[index] * w[1])) /(-1*w[2]);
    }
    //create y for w
    for(index = 0; index < w.length; index++) {
        y_w[index] = w[index];
    }
    x1_entered = new JTextField();
    x2_entered = new JTextField();
    Entered_X1 = new double[1];
    Entered_X2 = new double[1];
    Entered_X1[0] = Double.parseDouble(JOptionPane.showInputDialog(null,
    "Enter X1 feature of new sample"));
    Entered_X2[0] = Double.parseDouble(JOptionPane.showInputDialog(null,
    "Enter X2 feature of new sample"));
    double formula = (w[0] * 1) + (w[1] * Entered_X1[0]) + (w[2] *
    Entered_X2[0]);
    if(formula < 0) {
        JOptionPane.showMessageDialog(null, "The new sample belongs to
        FALSE class (too ripe)");
    }
    if(formula >= 0) {
        JOptionPane.showMessageDialog(null, "The new sample belongs to
        TRUE class (good fruit)");
    }
    //Menu Items
    show_decision_boundary_line = new JCheckBox("Show Decision Boundary
    Line", true);
    JMenuItem show_decision_bound = new JMenuItem("Show Decision
    Boundary");
    show_decision_bound.add(show_decision_boundary_line);
    //MenuBar
    JMenu view = new JMenu("view");
    view.add(show_decision_bound);
    JMenuBar menubar = new JMenuBar();
    JMenu file = new JMenu("File");
    JMenuItem Load_Training_Data = new JMenuItem("Load Training Data");
    JMenuItem Load_Test_Data = new JMenuItem("Load Test Data");
    JMenuItem Load_Weights = new JMenuItem("Load Weights");
    JMenuItem Save_Weights = new JMenuItem("Save Weights");
    JMenuItem Exit = new JMenuItem("Exit");
    file.add(Load_Training_Data);
    file.add(Load_Test_Data);
    file.add(Load_Weights);
    file.add(Save_Weights);
    file.add(Exit);
    menubar.add(file);
    menubar.add(view);
    frame.setJMenuBar(menubar);
    //plots
    plot1 = new JPlot2D(X1_true, X2_true);
    plot1.setTitle("Project 2: Fruit Classification");
    plot1.setXLabel("X1 Feature");
    plot1.setYLabel("X2 Feature");
    plot1.setLineState(false);
    plot1.setPlotType(JPlot2D.LINEAR);
    plot1.setGridState(JPlot2D.GRID_ON);
    plot1.setMarkerState(JPlot2D.MARKER_ON);
    plot1.setMarkerColor(Color.red);
    plot1.setMarkerStyle(JPlot2D.MARKER_CIRCLE);
    plot1.addCurve(X1_false, X2_false);
    plot1.setLineState(false);
    plot1.setPlotType(JPlot2D.LINEAR);
    plot1.setMarkerState(JPlot2D.MARKER_ON);
    plot1.setMarkerColor(Color.BLUE);
    plot1.setMarkerStyle(JPlot2D.MARKER_TRIANGLE);
    plot1.addCurve(Entered_X1, Entered_X2);
    plot1.setLineState(false);
    plot1.setPlotType(JPlot2D.LINEAR);
    plot1.setMarkerState(JPlot2D.MARKER_ON);
    plot1.setMarkerColor(Color.YELLOW);
    plot1.setMarkerStyle(JPlot2D.MARKER_SQUARE);
    plot1.addCurve(x, y);
    plot1.setPlotType(JPlot2D.LINEAR);
    plot1.setLineStyle(Plot2D.LINESTYLE_SOLID);
    plot1.setLineColor(Color.GREEN);
    plot1.setLineState(true);
    //Check Box
    show_training = new JCheckBox("Show Training", false);
    //Text Labels
    feature_1_text_label = new JLabel();
    feature_2_text_label = new JLabel();
    feature_1_text_label.setText("Feature 1");
    feature_2_text_label.setText("Feature 2");
    //combo box
    String[] view_data_samples = {"Show Test Data", "Show Training Data"};
    JComboBox<String> view_data_samples_combo_box = new
    JComboBox<>(view_data_samples);
    view_data_samples_combo_box.setPreferredSize(new Dimension(100,20));
    //Radio Button
    single_point = new JRadioButton("Single Point", true);
    multiple_points = new JRadioButton("Multiple Points", false);
    button_group = new ButtonGroup();
    button_group.add(multiple_points);
    button_group.add(single_point);
    //JButtons
    train = new JButton("Train");
    test = new JButton("Test");
    //Create JPanel
    testing_panel_text = new JPanel();
    panel_plot = new JPanel();
    panel_main = new JPanel();
    panel_ViewDataSamples = new JPanel();
    panel_TrainedWeights = new JPanel();
    panel_Testing = new JPanel();
    right_panel = new JPanel();
    bottom_right_panel = new JPanel();
    testing_panel_buttons = new JPanel();
    panel_main.setLayout(new BoxLayout(panel_main, BoxLayout.X_AXIS));
    panel_plot.setLayout(new BoxLayout(panel_plot, BoxLayout.Y_AXIS));
    panel_plot.add(plot1);
    panel_plot.setPreferredSize(new Dimension(1000,1000));
    panel_Testing.setPreferredSize(new Dimension(1200,2000));
    panel_ViewDataSamples.setPreferredSize(new Dimension(1200,6000));
    panel_TrainedWeights.setPreferredSize(new Dimension(1200,5500));
    bottom_right_panel.setPreferredSize(new Dimension(1200, 1000));
    bottom_right_panel.add(train, BorderLayout.WEST);
    bottom_right_panel.add(test, BorderLayout.EAST);
    right_panel.setLayout(new BoxLayout(right_panel, BoxLayout.Y_AXIS));
    panel_ViewDataSamples.setLayout(new BoxLayout(panel_ViewDataSamples,
    BoxLayout.Y_AXIS));
    panel_ViewDataSamples.add(view_data_samples_combo_box);
    String default_text = "";
    String default_text_initial = "Feature 1 \t\t\t\t Feature2 \n";
    for(int count = 0; count<10; count++) {
        default_text = ((default_text + X1_true[count] + "\t\t\t\t" +
        X2_true[count] + "\n"
        + X1_false[count] + "\t\t\t\t" + X2_false[count] + "\
        n"));
    }
    data_txt.setText(default_text_initial + default_text);
    panel_ViewDataSamples.add(data_txt, BorderLayout.CENTER);
    testing_panel_buttons.setLayout(new BoxLayout(testing_panel_buttons,
    BoxLayout.X_AXIS));
    testing_panel_buttons.add(multiple_points);
    testing_panel_buttons.add(single_point);
    testing_panel_text.setLayout(new BoxLayout(testing_panel_text,
    BoxLayout.X_AXIS));
    testing_panel_text.add(feature_1_text_label);
    testing_panel_text.add(X1, BorderLayout.EAST);
    testing_panel_text.add(feature_2_text_label);
    testing_panel_text.add(X2, BorderLayout.WEST);
    panel_Testing.setLayout(new BoxLayout(panel_Testing,
    BoxLayout.Y_AXIS));
    panel_Testing.add(testing_panel_buttons);
    panel_Testing.add(testing_panel_text);
    panel_TrainedWeights.add(testing);
    right_panel.add(panel_ViewDataSamples);
    right_panel.add(panel_TrainedWeights);
    right_panel.add(panel_Testing);
    right_panel.add(bottom_right_panel);
    panel_main.add(right_panel);
    //Borders
    panel_plot.setBorder(BorderFactory.createTitledBorder(
    BorderFactory.createEtchedBorder(), "Data Samples graph",
    TitledBorder.LEFT, TitledBorder.TOP));
    panel_ViewDataSamples.setBorder(BorderFactory.createTitledBorder(
    BorderFactory.createEtchedBorder(), "View Data Samples",
    TitledBorder.LEFT, TitledBorder.TOP));
    panel_TrainedWeights.setBorder(BorderFactory.createTitledBorder(
    BorderFactory.createEtchedBorder(), "Trained Weights",
    TitledBorder.LEFT, TitledBorder.TOP));
    panel_Testing.setBorder(BorderFactory.createTitledBorder(
    BorderFactory.createEtchedBorder(), "Testing Options",
    TitledBorder.LEFT, TitledBorder.TOP));
    frame.getContentPane().add(panel_plot, BorderLayout.WEST);
    panel_plot.add(show_training);
    frame.add(panel_main);
    frame.setVisible(true);
    }
}