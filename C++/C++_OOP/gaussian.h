class Gaussian
{
	private:
		float mu, sigma2;

	public:

		// constructor functions
		Gaussian ();
		Gaussian (float, float);

		// change value of average and standard deviation
		void setMu(float);
		void setSigma2(float);

		// output value of average and standard deviation
		float getMu();
		float getSigma2();

		// functions to evaluate
		float evaluate (float);
		Gaussian mul (Gaussian);
		Gaussian add (Gaussian);
};


// if mu and sigma2 have been made public,
// notice how it is no longer necessary
// to have getMu, getSigma2, setMu and setSigma2 functions
// because the object has direct access to those variables
