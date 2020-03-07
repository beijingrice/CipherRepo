#include <iostream>
#include <Windows.h>
#include <iostream>
using namespace std;

int main()
{
	cout << "字母表加密解密程序" << endl;
	cout << "加密输1, 解密输2" << endl;

	int serviceType = 0;

	//输入
	while (true)
	{
		cin >> serviceType;
		if (serviceType != 1 and serviceType != 2)
		{
			cout << "输入错误。请重新输入" << endl;
		}
		else
		{
			break;
		}
	}

	if (serviceType == 1)
	{
		system("cls");
		cout << "----------加密模式----------" << endl << endl;
		cout << "请输入要加密的串" << endl << endl;

		string encode;
		cin >> encode;
		cout << endl << "加密后：" << endl;
		
		cout << encode.size() << " ";
		for (int i = 0; i < encode.size(); i++)
		{
			cout << (int)encode[i] << " ";
		}
		cout << endl;
		system("pause");
		return 0;
	}
	if (serviceType == 2)
	{
		string mw;
		system("cls");
		cout << "----------解密模式----------" << endl << endl;
		cout << "请输入要解密的串" << endl;
		int gs = 0;
		cin >> gs;
		for (int i = 0; i < gs; i++)
		{
			int t = 0;
			cin >> t;
			mw.push_back((char)t);
		}

		cout << endl;
		cout << "明文：" << endl << mw << endl;
		
		system("pause");
		return 0;
	}
}