class AddTermIdToDocLookup < ActiveRecord::Migration
  def change
    add_column :doc_lookups, :term_id, :integer
  end
end
