class CreateDocuments < ActiveRecord::Migration
  def change
    create_table :documents do |t|
      t.integer :doc_id
      t.text :content
      t.timestamps
    end
  end
end
