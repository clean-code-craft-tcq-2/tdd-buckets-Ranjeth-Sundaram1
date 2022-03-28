def PrintSampleDetailsIntoConsole(samples, count):
    messagetoprint = (f"{samples[0]}-{samples[-1]}, {count}")
    print(messagetoprint)
    return(messagetoprint)

def SplitSamplesInToRanges(input_samples:list):
    in_range_samples = []
    sample_collections = []
    for sample in input_samples:
        is_Sample_in_Range = IsSampleHasContinuity(sample=sample, in_range_samples= in_range_samples)
        if is_Sample_in_Range:
            in_range_samples.append(sample)
            if sample == input_samples[-1]:
                sample_collections.append(in_range_samples)
        else:
            sample_collections.append(in_range_samples)
            in_range_samples = []
            in_range_samples.append(sample)
    return sample_collections
    
def IdentifyRangesofSamples(input_samples:list):
    if input_samples != []:
        sample_collections = SplitSamplesInToRanges(input_samples=RearrangeSamples(input_samples))
        filtered_samples = RemoveOccuranceOneSample(sample_collections)
        validation_report = []
        for one_collection in filtered_samples:
            validation_report.append(CountSamplesinOneRange(one_collection=one_collection))
        return validation_report
    return []
def CountSamplesinOneRange(one_collection=None):
    if one_collection != []:
        messagefromConsole = PrintSampleDetailsIntoConsole(one_collection, len(one_collection))
        return (len(one_collection), messagefromConsole)
    return(len(one_collection), "No data to print")

def IsSampleHasContinuity(sample, in_range_samples):
    if in_range_samples != []:
        if sample == int(in_range_samples[-1])+1 or sample == int(in_range_samples[-1]):
            return True
        return False
    return True

def RemoveOccuranceOneSample(sample_collections):
    filtered_samples = []
    for samples in sample_collections:
        if len(samples) > 1:
            filtered_samples.append(samples)
    return filtered_samples

def RearrangeSamples(input_samples):
    input_samples.sort()
    return(input_samples)
