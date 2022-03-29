import examine_samples

def IgnoreInvalidSamples(input_samples : list):
    if input_samples != []:
        samples_to_examine = [sample for sample in input_samples if sample in range(0, 1023)]
        return samples_to_examine
    return input_samples

def convertA2D_10BIntoAmps(input_samples: list):
    samples_to_examine = IgnoreInvalidSamples(input_samples)
    samples_to_examine = [abs(round(sample*30/1022) - 15) for sample in samples_to_examine]
    return samples_to_examine

def ExamineSamplesFrom_A2D(input_samples: list):
    samples_to_examine = convertA2D_10BIntoAmps(input_samples)
    print(samples_to_examine)
    found_sample_ranges = examine_samples.IdentifyRangesofSamples(samples_to_examine)
    print(found_sample_ranges)
    return found_sample_ranges
