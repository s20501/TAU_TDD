class hamming:
    @staticmethod
    def distance(gen_a, gen_b):
        if not gen_a and not gen_b:
            return 0
        if len(gen_a) != len(gen_b):
            raise ValueError("Not same length!")

        return sum(1 for a, b in zip(gen_a, gen_b) if a != b)
