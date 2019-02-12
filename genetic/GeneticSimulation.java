import java.util.Random;
public class GeneticSimulation
{
	public static int score = 0;
	public Data[] pops;
	public double[][] weights;
	public int population;
	public GeneticSimulation(double[][] weights, int population)
	{
		pops = new Data[population];
		for(int i = 0; i < population; i++)
			pops[i] = new Data(weights.length);
		this.population = population;
		this.weights = weights;
	}
	public Data run(double[] vals, int index, long endtime, boolean print, double Save, double Mutate, double Merge)
	{
		Random r = new Random();
		int save = (int)(Save * population);
		int mutate = (int)(Mutate * population);
		int merge = (int)(Merge * population);
		int random = population - save - mutate - merge;
		while(System.currentTimeMillis() < endtime) for(int i = 0; i < 1000; i++) //only check every 1000 iterations
		{
			//get new scores
			for(int j = 0; j < population; j++)
			{
				Data d = pops[j];
				for(int k = j - 1; k >= 0 && pops[k].getScore(weights) > d.getScore(weights); k--)
				{
					pops[k+1] = pops[k];
					pops[k] = d;
				}
			}
			//generate next population
			Data[] nextpops = new Data[population];
			for(int j = 0; j < save; j++)
				nextpops[j] = pops[j];
			for(int j = 0; j < mutate; j++)
				nextpops[j+save] = new Data(pops[(int)(r.nextDouble() * population)]).mutate(r);
			for(int j = 0; j < merge; j++)
				nextpops[j+save+mutate] = new Data(pops[(int)(r.nextDouble() * population)]).merge(r, pops[(int)(r.nextDouble() * population)]);
			for(int j = 0; j < random; j++)
				nextpops[j+save+mutate+merge] = new Data(pops[save + (int)(r.nextDouble() * (population - save))]);
			//update/print results if applicable
			vals[index] = Math.min(vals[index], pops[0].getScore(weights));
			if(print)
			{
				for(int j = 0; j < vals.length; j++)
					System.out.printf("%s%.2f",(j==0?"":" \t "),vals[j]);
				System.out.println();
			}
			pops = nextpops;
		}
		return pops[0];
	}
}
