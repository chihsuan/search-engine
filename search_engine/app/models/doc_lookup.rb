class DocLookup < ActiveRecord::Base
  belongs_to :term
  
  def self.look_up(keyword)
    term = Term.select("id, idf").where(:term => keyword).first
    if term.present?
      documents = DocLookup.where(:term_id => term['id']).limit(20)
      doc_ranking = self.rank_by_tf_idf(term, documents)
    else
      return []
    end
   
    return doc_ranking
  end

  def self.rank_by_tf_idf(term, documents)
    for doc in documents
      doc['tf'] = doc['tf'] * term['idf'] 
    end
    
    return documents.sort_by{|k| k['tf']}.reverse
  end

  def self.get_doc(id)
    return DocLookup.find(id)['doc_id']
  end

end
