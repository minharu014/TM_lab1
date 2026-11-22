from collections import Counter
import pandas as pd
from IPython.display import HTML, display

universal_freq = Counter(tag[1] for review in pos_tagged_reviews for tag in review)
penn_freq = Counter(tag[2] for review in pos_tagged_reviews for tag in review)

universal_df = pd.DataFrame(universal_freq.most_common(), columns=["POS", "Frequency"])
penn_df = pd.DataFrame(penn_freq.most_common(), columns=["POS", "Frequency"])

universal_df.insert(0, "No.", range(1, len(universal_df) + 1))
penn_df.insert(0, "No.", range(1, len(penn_df) + 1))

display(HTML(
    '<div style="display: flex; gap: 40px; align-items: flex-start;">'
    f'<div><h3>Universal POS</h3>{universal_df.to_html(index=False)}</div>'
    f'<div><h3>Penn POS</h3>{penn_df.to_html(index=False)}</div>'
    '</div>'
))