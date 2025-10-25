#include <iostream>
#include <iomanip>
#include <cmath>
#include <limits>
#include <thread>
#include <chrono>
#include <string>
#include <bitset>

#ifdef _WIN32
#include <windows.h>
void enableANSI() {
	HANDLE hOut = GetStdHandle(STD_OUTPUT_HANDLE);
	DWORD dwMode = 0;
	GetConsoleMode(hOut, &dwMode);
	dwMode |= 0x0004;
	SetConsoleMode(hOut, dwMode);
}
#else
void enableANSI() {}
#endif

void clearScreen() {
#ifdef _WIN32
	system("cls");
#else
	system("clear");
#endif
}

void slowPrint(std::string txt, int delay = 10) {
	for(char c: txt) {
		std::cout << c << std::flush;
		std::this_thread::sleep_for(std::chrono::milliseconds(delay));
	}
}

void wait() {
	std::cout << "\n\033[2;37mPress Enter to continue...\033[0m";
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	std::cin.get();
}

void header() {
	std::cout << "\033[1;36m";
	std::cout << "===========================================\n";
	std::cout << "           p'. CALCULATOR PRO        \n";
	std::cout << "===========================================\n";
	std::cout << "\033[0m";
}

void menu() {
	std::cout << "\n\033[1;33mChoose operation:\033[0m\n";
	std::cout << " 1. Basic (+, -, *, /)\n";
	std::cout << " 2. Power (^)\n";
	std::cout << " 3. Square root\n";
	std::cout << " 4. Trigonometric (sin, cos, tan)\n";
	std::cout << " 5. Percentage\n";
	std::cout << " 6. Logarithm (with base)\n";
	std::cout << " 7. Memory (store / recall / clear)\n";
	std::cout << " 8. Base Converter (bin / dec / hex)\n";
	std::cout << " 9. Factorial (!)\n";
	std::cout << "10. Equation Solver (ax + b = 0)\n";
	std::cout << "11. Average / Sum calculator\n";
	std::cout << "12. Quit\n";
}

// factorial helper
unsigned long long fact(int n) {
	if(n < 0) return 0;
	unsigned long long r = 1;
	for(int i=2; i<=n; ++i) r*=i;
	return r;
}

int main() {
	enableANSI();
	srand(time(nullptr));

	double memA = 0, memB = 0;
	bool running = true;

	while(running) {
		clearScreen();
		header();
		menu();

		int ch;
		std::cout << "\n\033[36mEnter choice: \033[0m";
		std::cin >> ch;

		if(std::cin.fail()) {
			std::cin.clear();
			std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
			continue;
		}

		double a,b,result=0;
		bool ok = true;

		switch(ch) {

		case 1: {
			char op;
			std::cout << "Enter (a op b): ";
			std::cin >> a >> op >> b;
			if(op=='+') result=a+b;
			else if(op=='-') result=a-b;
			else if(op=='*') result=a*b;
			else if(op=='/') {
				if(b==0) ok=false;
				else result=a/b;
			} else ok=false;
			break;
		}

		case 2:
			std::cout << "Base & exponent: ";
			std::cin >> a >> b;
			result = pow(a,b);
			break;

		case 3:
			std::cout << "Number: ";
			std::cin >> a;
			if(a<0) ok=false;
			else result = sqrt(a);
			break;

		case 4: {
			std::string func;
			std::cout << "Function (sin/cos/tan): ";
			std::cin >> func;
			std::cout << "Angle (deg): ";
			std::cin >> a;
			a = a * M_PI / 180.0;
			if(func=="sin") result = sin(a);
			else if(func=="cos") result = cos(a);
			else if(func=="tan") result = tan(a);
			else ok=false;
			break;
		}

		case 5:
			std::cout << "Value & percent: ";
			std::cin >> a >> b;
			result = (a*b)/100.0;
			break;

		case 6:
			std::cout << "Number & base: ";
			std::cin >> a >> b;
			if(a<=0 || b<=0 || b==1) ok=false;
			else result = log(a)/log(b);
			break;

		case 7: {
			std::cout << "\nMemory Slots:\n";
			std::cout << " A = " << memA << "\n B = " << memB << "\n";
			std::cout << "1.Store A  2.Store B  3.Recall A  4.Recall B  5.Clear all\n";
			int sub;
			std::cin >> sub;
			if(sub==1) {
				std::cout << "Enter value for A: ";
				std::cin >> memA;
				std::cout << "\033[1;32mSaved in A!\033[0m\n";
			} else if(sub==2) {
				std::cout << "Enter value for B: ";
				std::cin >> memB;
				std::cout << "\033[1;32mSaved in B!\033[0m\n";
			} else if(sub==3) {
				std::cout << "\033[1;36mA = \033[0m" << memA << "\n";
			} else if(sub==4) {
				std::cout << "\033[1;36mB = \033[0m" << memB << "\n";
			} else if(sub==5) {
				memA=memB=0;
				std::cout << "\033[1;31mAll cleared.\033[0m\n";
			} else ok=false;
			wait();
			continue;
		}

		case 8: {
			int type;
			std::cout << "1. Decimal b Binary/Hex\n2. Binary b Decimal\n3. Hex b Decimal\nChoose: ";
			std::cin >> type;
			if(type==1) {
				int num;
				std::cout << "Enter decimal: ";
				std::cin >> num;
				std::cout << "Binary: " << std::bitset<16>(num)
				          << "\nHex: " << std::hex << num << std::dec << "\n";
			} else if(type==2) {
				std::string bin;
				std::cout << "Enter binary: ";
				std::cin >> bin;
				int dec = std::stoi(bin, nullptr, 2);
				std::cout << "Decimal: " << dec << "\n";
			} else if(type==3) {
				std::string hx;
				std::cout << "Enter hex: ";
				std::cin >> hx;
				int dec = std::stoi(hx, nullptr, 16);
				std::cout << "Decimal: " << dec << "\n";
			} else ok=false;
			wait();
			continue;
		}

		case 9: {
			int n;
			std::cout << "Enter n (<=20 recommended): ";
			std::cin >> n;
			if(n<0) ok=false;
			else result = fact(n);
			break;
		}

		case 10: {
			std::cout << "Solve ax + b = 0\nEnter a and b: ";
			std::cin >> a >> b;
			if(a==0) ok=false;
			else result = -b/a;
			break;
		}

		case 11: {
			int count;
			std::cout << "How many numbers? ";
			std::cin >> count;
			if(count<=0) {
				ok=false;
				break;
			}
			double sum=0, val;
			for(int i=1; i<=count; i++) {
				std::cout << "Enter #" << i << ": ";
				std::cin >> val;
				sum+=val;
			}
			std::cout << "Sum = " << sum << "\n";
			std::cout << "Average = " << sum/count << "\n";
			wait();
			continue;
		}

		case 12:
			clearScreen();
			slowPrint("\033[1;32mExiting Calculator...\033[0m\n", 25);
			running=false;
			continue;

		default:
			ok=false;
		}

		if(ok) {
			std::cout << "\n\033[1;32mResult:\033[0m " << std::fixed << std::setprecision(6) << result << "\n";
		} else {
			std::cout << "\n\033[1;31mInvalid input or operation.\033[0m\n";
		}

		wait();
	}

	clearScreen();
	std::cout << "\033[1;34mGoodbye, friend!\033[0m\n";
	std::this_thread::sleep_for(std::chrono::milliseconds(400));
	return 0;
}

