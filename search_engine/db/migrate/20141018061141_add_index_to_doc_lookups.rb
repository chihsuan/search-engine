class AddIndexToDocLookups < ActiveRecord::Migration
  def change
    add_index :doc_lookups, :term_id
  end
end
