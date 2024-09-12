#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <ctype.h>
#include <complex.h> // Include for complex numbers

void print_menu();
double evaluate_expression(const char* expr);
double parse_number(const char** expr);
double parse_parentheses(const char** expr);
double parse_factor(const char** expr);
double parse_term(const char** expr);
double parse_expression(const char** expr);
double solve_linear_equation(double a, double b);
void solve_quadratic_equation(double a, double b, double c);
double evaluate_trigonometric_function(const char* func, double x);
void convert_degrees_radians();
void handle_constants(double* num1);
void calculate_statistics();
void matrix_operations();
void memory_operations();
double factorial(int n);
double evaluate_logarithmic_function(const char* func, double x);
int is_prime(int num);
void complex_operations(); // Function for complex number operations
void unit_conversion(); // Function for unit conversions

double memory = 0; 

void print_menu() {
    printf("Select operation:\n");
    // Existing menu options...
    printf(" complex for complex number operations\n");
    printf(" convert for unit conversions\n");
    printf(" Enter operation: ");
}

// Complex number operations function
void complex_operations() {
    double real1, imag1, real2, imag2;
    char op;
    printf("Enter first complex number (real and imaginary): ");
    scanf("%lf %lf", &real1, &imag1);
    printf("Enter second complex number (real and imaginary): ");
    scanf("%lf %lf", &real2, &imag2);
    printf("Enter operation (+, -, *, /): ");
    scanf(" %c", &op);

    double complex num1 = real1 + imag1 * I;
    double complex num2 = real2 + imag2 * I;
    double complex result;

    if (op == '+') {
        result = num1 + num2;
    } else if (op == '-') {
        result = num1 - num2;
    } else if (op == '*') {
        result = num1 * num2;
    } else if (op == '/') {
        result = num1 / num2;
    } else {
        printf("Invalid operation.\n");
        return;
    }

    printf("Result: %.2lf + %.2lfi\n", creal(result), cimag(result));
}

// Unit conversion function
void unit_conversion() {
    int choice;
    double value;
    printf("Unit conversion menu:\n");
    printf("1. Inches to Centimeters\n");
    printf("2. Centimeters to Inches\n");
    printf("3. Kilograms to Pounds\n");
    printf("4. Pounds to Kilograms\n");
    printf("5. Celsius to Fahrenheit\n");
    printf("6. Fahrenheit to Celsius\n");
    printf("Choose an option: ");
    scanf("%d", &choice);

    switch (choice) {
        case 1:
            printf("Enter inches: ");
            scanf("%lf", &value);
            printf("Centimeters: %.2lf\n", value * 2.54);
            break;
        case 2:
            printf("Enter centimeters: ");
            scanf("%lf", &value);
            printf("Inches: %.2lf\n", value / 2.54);
            break;
        case 3:
            printf("Enter kilograms: ");
            scanf("%lf", &value);
            printf("Pounds: %.2lf\n", value * 2.20462);
            break;
        case 4:
            printf("Enter pounds: ");
            scanf("%lf", &value);
            printf("Kilograms: %.2lf\n", value / 2.20462);
            break;
        case 5:
            printf("Enter Celsius: ");
            scanf("%lf", &value);
            printf("Fahrenheit: %.2lf\n", value * 9 / 5 + 32);
            break;
        case 6:
            printf("Enter Fahrenheit: ");
            scanf("%lf", &value);
            printf("Celsius: %.2lf\n", (value - 32) * 5 / 9);
            break;
        default:
            printf("Invalid choice.\n");
            break;
    }
}

int main() {
    char input[256];
    char operation[10];
    double num1, num2, result;

    print_menu();

    while (1) {
        printf("> ");
        if (!fgets(input, sizeof(input), stdin)) {
            printf("Error reading input.\n");
            break;
        }

        // Strip newline
        input[strcspn(input, "\n")] = 0;

        sscanf(input, "%s", operation);

        if (strcmp(operation, "exit") == 0) {
            break;
        } else if (strcmp(operation, "sqrt") == 0) {
            printf("Enter a number: ");
            scanf("%lf", &num1);
            if (num1 < 0) {
                printf("Error! Negative number for square root.\n");
            } else {
                result = sqrt(num1);
                printf("Result: %.2lf\n", result);
            }
        } else if (strcmp(operation, "complex") == 0) {
            complex_operations();
        } else if (strcmp(operation, "convert") == 0) {
            unit_conversion();
        } else {
            // Existing operations...
            const char* p = input;
            result = evaluate_expression(p);
            printf("Result: %.2lf\n", result);
        }

        while (getchar() != '\n');
    }

    return 0;
}
