import java.util.Random;
public class Data
{
	public int[] pairings;
	public Data(int size)
	{
		pairings = new int[size];
		for(int i = 0; i < pairings.length; i++)
			pairings[i] = -1;
	}
	public Data(Data other)
	{
		pairings = new int[other.pairings.length];
		for(int i = 0; i < pairings.length; i++)
			pairings[i] = other.pairings[i];
	}
	double total = -1;
	public double getScore(double[][] ratings)
	{
		if(total > -0.5)
			return total;
		total = 0;
		for(int i = 0; i < pairings.length; i++)
		{
			if(pairings[i] == -1)
				total+=ratings[i][i]*ratings[i][i];
			else
				total+=ratings[i][pairings[i]]*ratings[i][pairings[i]];
		}
		return total;
	}
	public void pair(int a, int b)
	{
		int t = pairings[b];
		int t2 = pairings[a];
		pairings[a] = b;
		pairings[b] = a;
		if(t == -1 && t2 != -1)
			pairings[t2] = -1;
		else if(t != -1 && t2 == -1)
			pairings[t] = -1;
		else if(t != -1 && t2 != -1)
		{
			pairings[t] = t2;
			pairings[t2] = t;
		}
	}
	public void mutateOnce(Random rand)
	{
		int a = (int)(rand.nextDouble() * pairings.length);
		int b = a;
		while(a == b) b = (int)(rand.nextDouble() * pairings.length);
		pair(a, b);
	}
	public Data mutate(Random rand)
	{
		mutateOnce(rand);
		for(int i = 0; i < 5; i++)
			if(rand.nextDouble() < 0.3)
				mutateOnce(rand);
		return this;
	}
	public Data merge(Random rand, Data other)
	{
		for(int i = 0; i < pairings.length; i++)
			if(other.pairings[i] != -1 && rand.nextDouble() < 0.2)
				pair(i, other.pairings[i]);
		return this;
	}
}
