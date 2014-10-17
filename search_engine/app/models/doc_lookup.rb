class DocLookup < ActiveRecord::Base
  belongs_to :term
  
  def self.is_zh(c)
    c_unicode = c.ord
    zh_range = [[0x2e80, 0x33ff], [0xff00, 0xffef], [0x4e00, 0x9fbb], \
                [0xf900, 0xfad9], [0x20000, 0x2a6d6], [0x2f800, 0x2fa1d]]

    zh_range.each do |lower, upper|
      if c_unicode >= lower and c_unicode <= upper
        puts 'is zh'
        return true
      end
    end
    return false
  end

  def self.look_up(query_terms)

    #exec("python is_zh.py " + query_terms[0])
    if self.is_zh(query_terms[0])
      keywords = self.n_gram(query_terms, 2)
    else
      keywords = query_terms.split(' ')
    end
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

  def self.n_gram(query, n)
    tokens = []
    stop = query.length - n + 1
    for i in 0..stop
      tokens << query[i..i+n-1]
    end
    puts tokens
    return tokens
  end
end
