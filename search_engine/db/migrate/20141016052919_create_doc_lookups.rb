class CreateDocLookups < ActiveRecord::Migration
  def change
    create_table :doc_lookups do |t|
      t.integer :doc_id
      t.integer :frequency
      t.float :weight
      t.timestamps
    end
  end
end
