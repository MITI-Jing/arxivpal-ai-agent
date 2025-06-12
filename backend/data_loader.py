from datasets import load_dataset

def get_sample_paper(index=0):
    dataset = load_dataset("ccdv/arxiv-summarization", split="train[:100]")
    return dataset[index]["article"], dataset[index]["abstract"]

if __name__ == "__main__":
    article, abstract = get_sample_paper()
    print("Article snippet:", article[501:1500])
    print("Abstract:", abstract)
    print("Total papers in sample:", len(get_sample_paper())) 
