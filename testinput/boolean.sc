internal byte foo;

void comparisons(byte param)
{
	if (boolean.foo > 3 != 2 < param || 5 <= 4 && (!(3 >= 4) == (2 != 5)) && !boolean.foo@3 == true != false)
	{
		boolean.foo = 3;
	}
	boolean.foo@4 = true;
	boolean.foo@3 = false;
}
