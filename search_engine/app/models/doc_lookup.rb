class DocLookup < ActiveRecord::Base
  belongs_to :term
  
  def self.look_up(query_terms)

    keywords = query_terms.split(' ')
    doc_ranking = nil

    for keyword in keywords
      term = Term.select("id, idf").where(:term => keyword.stem).first
      if term.present?
        documents = DocLookup.where(:term_id => term['id']).limit(20)
        doc_hash = documents.index_by(&:id)
        doc_ranking = self.rank_by_tf_idf(term, doc_hash, doc_ranking)
      end
    end

    return doc_ranking
  end

  def self.rank_by_tf_idf(term, doc_hash, doc_ranking)

    doc_hash.each do |key, values|
      if doc_ranking.present? and doc_ranking.has_key?(key)
        values['tf'] = values['tf'] * term['idf'] + doc_ranking[key]['tf']
      else
        values['tf'] = values['tf'] * term['idf'] 
      end
    end
    

    return doc_hash.sort_by{|k, v| v['tf']}.reverse
  end

  def self.get_doc(id)
    return DocLookup.find(id)['doc_id']
  end

end
